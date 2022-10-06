import editdistance
data = ['New', 'New']
for record in data:
    dist = editdistance.eval(record, 'News')
    print('Edit Distance for %s and %s is %d' % (record, 'edwin', dist))