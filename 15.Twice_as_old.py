def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)
        
print(twice_as_old(36,7))



def to_jaden_case(string):
    # return " ".join(map(lambda x: x.capitalize(), string.split()))
    return ' '.join(word.capitalize() for word in string.split())

quote = "How can mirrors be real if our eyes aren't real"

print(to_jaden_case(quote))