# TaskApp

Tables:
1.	Users
o	user_id (Primary Key)
o	firstname
o	lastname
o	job
o	username
o	email
o	password
o	profile_image (e.g., name, profile picture)
2.	Tasks
o	task_id (Primary Key)
o	user (Foreign Key referencing Users table)
o	title
o	description
o	task_category(Foreign Key referencing Category)
o	due_date
o	priority (e.g., high, medium, low)
o	status (e.g., incomplete, complete)
o	created_at
o	updated_at
3.	Task Categories
o	category_id (Primary Key)
o	name
o	color (for categorizing tasks with different colors)
4.	Subtasks (Optional)
o	subtask_id (Primary Key)
o	task_id (Foreign Key referencing Tasks table)
o	title
o	description
o	completed (boolean to indicate whether the subtask is completed or not)
Relationships:
•	Each user can have multiple tasks.
•	Each task can belong to one user.
•	Each task can be associated with one category.
•	Each category belongs to one task.
•	Tasks can have optional subtasks, which are related to a specific task.
