import streamlit as st
from datetime import date
import uuid

st.set_page_config(
    page_title="Study Planner & To-Do",
    page_icon="📚",
    layout="wide"
)

# ---------- Page styling ----------
st.title("📚 Study Planner & To-Do")
st.caption("Plan your study sessions, track deadlines, and celebrate your progress.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---------- Add task ----------
st.subheader("➕ Add a study task")

with st.form("add_task_form", clear_on_submit=True):
    task_title = st.text_input("Task name", placeholder="e.g., Revise Unit 3 of Machine Learning")
    col1, col2, col3 = st.columns(3)

    with col1:
        subject = st.text_input("Subject", placeholder="e.g., Machine Learning")
    with col2:
        due_date = st.date_input("Due date", value=date.today())
    with col3:
        priority = st.selectbox("Priority", ["High", "Medium", "Low"], index=1)

    notes = st.text_input("Notes (optional)", placeholder="e.g., Review lecture notes and solve 5 questions")
    submitted = st.form_submit_button("Add task", use_container_width=True)

    if submitted:
        if not task_title.strip():
            st.error("Please enter a task name.")
        else:
            st.session_state.tasks.append({
                "id": str(uuid.uuid4()),
                "title": task_title.strip(),
                "subject": subject.strip() or "General",
                "due_date": due_date,
                "priority": priority,
                "notes": notes.strip(),
                "done": False
            })
            st.success("Task added to your planner!")
            st.rerun()

st.divider()

# ---------- Summary ----------
tasks = st.session_state.tasks
total = len(tasks)
completed = sum(1 for task in tasks if task["done"])
pending = total - completed
overdue = sum(
    1 for task in tasks
    if not task["done"] and task["due_date"] < date.today()
)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total tasks", total)
m2.metric("Completed", completed)
m3.metric("Pending", pending)
m4.metric("Overdue", overdue)

st.divider()

# ---------- Task list and filters ----------
st.subheader("🗓️ My study tasks")

filter_col, sort_col = st.columns(2)
with filter_col:
    status_filter = st.selectbox(
        "Show tasks",
        ["All", "Pending", "Completed", "Overdue"]
    )
with sort_col:
    sort_by = st.selectbox(
        "Sort by",
        ["Due date", "Priority", "Subject"]
    )

priority_order = {"High": 0, "Medium": 1, "Low": 2}
visible_tasks = tasks[:]

if status_filter == "Pending":
    visible_tasks = [t for t in visible_tasks if not t["done"]]
elif status_filter == "Completed":
    visible_tasks = [t for t in visible_tasks if t["done"]]
elif status_filter == "Overdue":
    visible_tasks = [
        t for t in visible_tasks
        if not t["done"] and t["due_date"] < date.today()
    ]

if sort_by == "Due date":
    visible_tasks.sort(key=lambda t: (t["due_date"], t["done"]))
elif sort_by == "Priority":
    visible_tasks.sort(key=lambda t: (priority_order[t["priority"]], t["due_date"]))
else:
    visible_tasks.sort(key=lambda t: t["subject"].lower())

if not visible_tasks:
    st.info("No tasks to show yet. Add a task above to get started.")
else:
    for task in visible_tasks:
        with st.container(border=True):
            left, middle, right = st.columns([0.08, 0.72, 0.20])

            with left:
                new_done = st.checkbox(
                    "Complete task",
                    value=task["done"],
                    key=f"done_{task['id']}",
                    label_visibility="collapsed"
                )
                if new_done != task["done"]:
                    for stored_task in st.session_state.tasks:
                        if stored_task["id"] == task["id"]:
                            stored_task["done"] = new_done
                            break
                    st.rerun()

            with middle:
                if task["done"]:
                    st.markdown(f"~~**{task['title']}**~~")
                else:
                    st.markdown(f"**{task['title']}**")
                st.caption(
                    f"📘 {task['subject']}  ·  📅 Due: {task['due_date'].strftime('%d %b %Y')}  ·  "
                    f"Priority: {task['priority']}"
                )
                if task["notes"]:
                    st.write(task["notes"])
                if not task["done"] and task["due_date"] < date.today():
                    st.warning("This task is overdue.")

            with right:
                if st.button("🗑️ Delete", key=f"delete_{task['id']}", use_container_width=True):
                    st.session_state.tasks = [
                        t for t in st.session_state.tasks if t["id"] != task["id"]
                    ]
                    st.rerun()

st.divider()
if st.session_state.tasks:
    if st.button("Clear all completed tasks"):
        st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
        st.rerun()

st.caption(
    "Note: This beginner version stores tasks in the current Streamlit session. "
    "Tasks may reset when the app session restarts; persistent storage can be added later."
)
