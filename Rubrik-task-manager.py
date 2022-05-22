# An engineer can only handle a fixed number of tasks a day. Design a data strcutre to simulate the to-do-list.
# Tasks are handled on a FIFO basis. Tasks are unique.
#
# The data structure needs to expose below APIs:
# void add(string task) # O(1) performance, raise an error if limit is reached
# void handle() # O(1) performance, a task is handled and removed from the to-do-list
# string print() # print the data structure, so we know which tasks are in the list, and in which order
# void promote() # get a promotion hence number of tasks can be handled is increased
# void prioritize(string task) # prioritize the task despite FIFO,
# task is handled and removed from the to-do-list. Can you achieve O(1) time?
# write test code to validate the APIs
# discuss thread-safety of the APIs
