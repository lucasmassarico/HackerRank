# https://www.hackerrank.com/challenges/cats-and-a-mouse
def cat_and_mouse(x, y, z):

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        print(cat_and_mouse(x, y, z))
