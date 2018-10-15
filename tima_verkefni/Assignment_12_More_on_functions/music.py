def music_func(music="Classic Rock", group="The Beatles", singer="Freddie Mercury"):
    print("The best kind of music is", music)
    print("The best music group is", group)
    print("The best lead vocalist is", singer)


# definition for music_func goes here

def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()


main()
