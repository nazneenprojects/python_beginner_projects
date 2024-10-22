""" Create a Student Account object using the Builder Pattern
You're given a code template consisting of Builder Pattern class snippets.
Your task: Flesh out the provided code stub to implement the Builder Pattern and
instantiate the Student Account class.
Parameters
  Builder : object
  Result
Student Account : object with the following methods
  add_type()
  add_id()
  add_clearance()

Student Account object using the Builder Pattern:

1. StudentAccount class - The main class whose instances will be built.
2. StudentAccountBuilder class - The builder class responsible for building the StudentAccount object step-by-step.
"""

class StudentAccount:
    def __init__(self, student_type=None, student_id=None, clearance_level=None):
        self.student_type = student_type
        self.student_id = student_id
        self.clearance_level = clearance_level

    def __str__(self):
        return f"StudentAccount(type={self.student_type}, id={self.student_id}, clearance={self.clearance_level})"


class StudentAccountBuilder:
    def __init__(self):
        # Initialize a new StudentAccount object
        self.student_account = StudentAccount()

    def add_type(self, student_type):
        # Set the student_type field of the StudentAccount
        self.student_account.student_type = student_type
        return self  # Return self to allow chaining of methods

    def add_id(self, student_id):
        # Set the student_id field of the StudentAccount
        self.student_account.student_id = student_id
        return self  # Return self to allow chaining of methods

    def add_clearance(self, clearance_level):
        # Set the clearance_level field of the StudentAccount
        self.student_account.clearance_level = clearance_level
        return self  # Return self to allow chaining of methods

    def build(self):
        # Return the fully built StudentAccount object
        return self.student_account


# Example usage of the Builder Pattern to create a StudentAccount object
builder = StudentAccountBuilder()
student_account = (
    builder
    .add_type("Undergraduate")
    .add_id("123456")
    .add_clearance("Full")
    .build()
)

print(student_account)
