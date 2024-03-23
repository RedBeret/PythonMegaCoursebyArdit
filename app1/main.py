user_prompt = "Enter your todo: "
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
#
# todo = [todo1, todo2, todo3, "hello"]
# print(todo)
#
# print(type(user_prompt))

todo = []
# while True:
#     user_input = input(user_prompt)
#     if user_input == "exit":
#         break
#     todo.append(user_input)
# print(todo.capitalize())

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter your todo: ")
            todo.append(todo)
        case "show":
            for item in todo:
                print(item)
        case "exit":
            break
print("Goodbye!")