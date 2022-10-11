class Game:
    def __init__(self):
        while True:

            print(''' welcome, choose game number ...
            1 : divided by game
            2 : remove duplicate game ''')
            user_choice = int(input('Enter Game Number :'))


            if user_choice == 1:
                x = int(input('Enter first Number :'))
                y = int(input('Enter first Number :'))
                self.divide_by(x,y)
            elif user_choice == 2:
                sentence = input('Enter Your Sentence :')
                self.no_duplicate(sentence)

            play_again = input('Press y to play again , n to exit :')
            if play_again == 'n':
                print('Godbye...')
                break

    def divide_by(self,x,y):
        for n in range(1,101):
            if n%x == 0 and n%y == 0:
                print(n)
    def no_duplicate(self,sentence):
        words=[]
        for x in sentence.split(' '):
            if x not in words:
                words.append(x)
        print(' '.join(words))

g = Game()        

