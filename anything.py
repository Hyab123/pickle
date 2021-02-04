instructor = {}

jacore_leader = {}
andrew_leader = {}
aris_leader = {}
richard_leader = {}
gaberiel_leader = {}

jacore_members = {}
andrew_members = {}
aris_members = {}
richard_members = {}
gaberiel_members = {}

jacore_members['Jacore Baptiste'] = '(845) 200-6250'
jacore_members['Moussa Ndiaye'] = '(123) 456-7890'
jacore_members['Morris Jones'] = '(925) 286-5922'
jacore_members['Prince Fields'] = '(510) 472-0804'
jacore_members['Akari Johnson'] = '(510) 500-2206'

andrew_members['Andrew Lubega'] = '(925) 727-4611'
andrew_members['Mallick Abdullah'] = '(510) 409-8755'
andrew_members['Ronin Youngjones'] = '(415) 910-3415'
andrew_members['Glenn Ivory'] = '(510) 328-8290'

aris_members['Aris Carter'] = '(510) 229-6359'
aris_members['Hyab isayas'] = '(510) 612-3737'
aris_members['Milan Kral'] = ' (510) 816-3232'
aris_members['Maurice Richardson'] = '(510) 424-7789'
aris_members['Zyion Williams'] = '(510) 480-5785'

richard_members['Richard Kamau'] = '(510) 228-5623'
richard_members['Kymari Rhodes'] = '    (510) 575-1982'
richard_members['Josiah Johnson'] = ' (510) 860-5112'

richard_members['Richard Kamau'] = '(510) 228-5623'
richard_members['Kymari Rhodes'] = '(510) 575-1982'
richard_members['Josiah Johnson'] = ' (510) 860-5112'
richard_members['Matthew Dudley'] = '(510) 816-2411'

gaberiel_members['Gabriel Reader'] = '(510) 326-5834'
gaberiel_members['Emmanuel Torbor'] = '(510) 934-4133'
gaberiel_members['David Brickley'] = ' (510) 631-6288'
gaberiel_members['Myles Wilkerson'] = '(510) 500-7266'

jacore_leader['Jacore'] = jacore_members
andrew_leader['Andrew'] = andrew_members
aris_leader['Aris'] = aris_members
richard_leader['Richard'] = richard_members
gaberiel_leader['Gaberial'] = gaberiel_members

instructor['Baba'] = jacore_leader
instructor["Hodari"] = andrew_leader
instructor["David"] = aris_leader
instructor["Paris"] = gaberiel_leader
instructor["Akeem"] = richard_leader
#print(instructor)

for instructor, pod_leader in instructor.items():
    print ("Instructor:", instructor)

    for pod_leader, pod_member in pod_leader.items():
        print ("Pod_leader:", pod_leader)
        for pod_member, phone_number in pod_member.items():

            print(pod_member, phone_number);
        print("\n")
