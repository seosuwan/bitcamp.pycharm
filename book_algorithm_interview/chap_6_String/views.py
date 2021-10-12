from book_algorithm_interview.string_tutorial.models import Palindrome

if __name__ == '__main__':
    pal = Palindrome()
    ls = pal.str_to_list("A man, a plan, a canal: Panama")
    resversed_ls = pal.reverse_list(ls)

    print(resversed_ls)