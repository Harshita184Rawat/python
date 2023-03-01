# Remove an empty tuple from a given list of tuples. 
'''
Examples:

Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),()]
Output : [('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (", ")]

Input : tuples = [(",",'8'), (), ('0', '00', '000'), ('birbal', ”, '45'), ("), (),  (","),()]
Output : [(", ", '8'), ('0', '00', '000'), ('birbal', ", '45'), (", ")]

'''
list_of_tuples=[(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),()]
def remove_empty_tuple(list):
    while () in list_of_tuples:
        list_of_tuples.remove(())
    print(list_of_tuples)

remove_empty_tuple(list_of_tuples)