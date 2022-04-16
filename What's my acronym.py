print(".".join([ i for i in input() if i.isupper() and i.isalpha()]))# Example
#Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user. For example:

#Input -> As Soon As Possible. Output -> ASAP.
#Input -> World Health Organization. Output -> WHO.
#Input -> Absent Without Leave. Output -> AWOL.
acronym = ""

full_meaning = str(input("Write Full meaning ,and I'm gonna change it to acronym \n(New word should be a big letter and space ) : "))
for i in full_meaning:
    num = ''
    if i.isdigit():
        num +=i
        print("Sory we can't make acronym of:\n{} ".format(num))
    if i.isupper():
        acronym += i + '.'

print("You're acronimy of :\n{}\nis\n{}".format(full_meaning,(acronym[:-1])))

# Or oneline
print(".".join([ i for i in input("Write Full meaning ,and I'm gonna change it to acronym \n(New word should be a big letter and space ) : ") if i.isupper() and i.isalpha()]))
