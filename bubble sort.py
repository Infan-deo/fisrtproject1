
def bubble_sort(age):
    for i in range(len(age)-1,0,-1): # I know it is difficult to understand check out the link
        for j in range(i):
            if age[j] > age[j+1]:
                temp = age[j]
                age[j] =age[j+1]
                age[j+1] = temp
# https://www.youtube.com/watch?v=Vca808JTbI8&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=75
        print(age)
age =[3,4,2,9,1,7]

bubble_sort(age)
print(age)