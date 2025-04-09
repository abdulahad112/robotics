import streamlit as st

# Initialize session state
if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

st.title("📝 Simple To-Do List")

# Add new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.todo_list.append({"task": new_task.strip(), "completed": False})
        st.success("Task added!")
    else:
        st.warning("Please enter a valid task.")

# View and manage tasks
st.subheader("Your Tasks")
if not st.session_state.todo_list:
    st.info("No tasks yet.")
else:
    for i, task in enumerate(st.session_state.todo_list):
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            checked = st.checkbox("", key=f"task_{i}", value=task['completed'])
            st.session_state.todo_list[i]['completed'] = checked
        with col2:
            task_text = f"~~{task['task']}~~" if task['completed'] else task['task']
            st.markdown(task_text)

# Delete completed tasks
if st.button("🗑️ Delete Completed Tasks"):
    st.session_state.todo_list = [t for t in st.session_state.todo_list if not t['completed']]
    st.success("Completed tasks removed.")

