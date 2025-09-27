class InputUtil:
    @staticmethod
    def get_user_input(prompt : str):
        user_input = input(prompt)
        while not user_input or user_input.isspace():
            print('Invalid input. Try again')
            user_input = input(prompt)
        return user_input
        # while True:
        #     user_input = input(prompt)
        #     if user_input and not user_input.isspace():
        #         return user_input
        #     print('Invalid input. Try again.')