from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        if task not in self.tasks:
            self.tasks.append(task)

            return f"Task {task.details()} is added to the section" #????????

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        number_of_tasks = 0
        for task in self.tasks:
            if task.completed:
                number_of_tasks += 1
                self.tasks.remove(task)

        return f"Cleared {number_of_tasks} tasks."

    def view_section(self):
        tasks_with_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}: \n" \
               f"{tasks_with_details}"

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

