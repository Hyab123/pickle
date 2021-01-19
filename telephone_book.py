import pickle

# 1. Leader Numbers

leader = {}
leader['Jacore Baptiste'] = '(845) 200-6250'
leader['Andrew'] = '(925) 727-4611'
leader['Gabriel'] = '(510) 613-6288'
leader['Aris'] = '(510) 229-6359'
leader['Richard'] = '(510) 228-5623'

# 2. create/open pod_nbrs.pkl file

pod_file = open('pod_nbrs.pkl', 'wb')

# 3. Write POD Leader number to a file

pickle.dump(leader, pod_file)

# 4. Member Numbers

member = {}
member['Hyab'] = '(510) 612-3737'
member['Aris'] = '(510) 229-6359'
member['Milan'] = '(510) 816-3232'
member['Maurice'] = '(510) 424-7789'
member ['Zyion'] = '(510) 480-5785'

# 5. Write Member numbers to pod_file

pickle.dump(member, pod_file)

# 6. Close pod_file

pod_file.close()

# 7. Open pod.file

pod_file = open('pod_nbrs.pkl', 'rb')

# 8. Leader numbers

print ('Leaders')
for (key, value) in leader.items():
    print (key, value)

print ('\n')

# 9. Print POD members

print ('Member')
for (key, value) in member.items():
    print (key, value)

print ('\n')

# 10. Close pod_file

pod_file.close()
