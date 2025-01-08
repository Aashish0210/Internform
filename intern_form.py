import streamlit as st
import requests
import json

# 'https://script.google.com/macros/s/AKfycbx5fs_SExSWtCpyYEM6Hhjw8Plj4VyVtD6-tUD7Ly0xudiVZNZpNtsqvrVqHEh3uOo/exec'


# Replace with your deployed Google Apps Script Web App URL
google_script_url = 'https://script.google.com/macros/s/AKfycbzxxiyx9UtFrHyzfQ_uW6y2Jmmk5ujT7KNIj-7R0b6-ZayBjIJAC9zPHaY6DBoFLf0/exec'

st.title("Task Management Form")
st.markdown("Fill out the form below to submit task details to Google Sheets.")

# Create a form using Streamlit
with st.form("task_form"):
    date = st.date_input("Date")
    name = st.text_input("Name")
    task_name = st.text_input("Task Name")
    task_type = st.selectbox("Task Type", ["Development", "Testing", "Design", "Other"])
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    assigned_by = st.text_input("Assigned By")
    task_status = st.selectbox("Task Status", ["Not Started", "In Progress", "Completed"])
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    estimated_hours = st.number_input("Estimated Hours", min_value=0, step=1)
    actual_hours_spent = st.number_input("Actual Hours Spent", min_value=0, step=1)
    progress_description = st.text_area("Progress Description")
    issues_challenges = st.text_area("Issues/Challenges")
    support_required = st.selectbox("Support Required", ["Yes", "No"])
    reviewer_name = st.text_input("Reviewer Name")
    review_status = st.selectbox("Review Status", ["Not Reviewed", "Reviewed", "Approved"])
    comments_feedback = st.text_area("Comments/Feedback")
    next_steps = st.text_area("Next Steps")
    additional_notes = st.text_area("Additional Notes")
    
    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        form_data = {
            "date": str(date),
            "name": name,
            "taskName": task_name,
            "taskType": task_type,
            "priority": priority,
            "assignedBy": assigned_by,
            "taskStatus": task_status,
            "startDate": str(start_date),
            "endDate": str(end_date),
            "estimatedHours": int(estimated_hours),
            "actualHoursSpent": int(actual_hours_spent),
            "progressDescription": progress_description,
            "issuesChallenges": issues_challenges,
            "supportRequired": support_required,
            "reviewerName": reviewer_name,
            "reviewStatus": review_status,
            "commentsFeedback": comments_feedback,
            "nextSteps": next_steps,
            "additionalNotes": additional_notes
        }
        
        # Send data to Google Apps Script
        try:
            response = requests.post(
                google_script_url,
                json=form_data,
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                st.success("Data successfully sent to Google Sheet!")
                st.json(response.json())
            else:
                st.error(f"Failed to send data: {response.status_code}")
                st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
