"""
Install future package where your script is present.
Implement basic functions of Queue - putting items into queue and reading them.
Use logging from Day 7 and log the items you write and read from queue.
Note: make sure the future package isn't installed/present in your Python core packages.
"""
import logging
logging.basicConfig(
    filename="example.log",
    level=logging.DEBUG,
)
class Queue:  
  
    def __init__(self):  
        self.queue = list()  
    
    def add_element(self,val):  
# Insert method to add element  
        if val not in self.queue:  
            self.queue.insert(0,val)
            logging.info("Added the element %s",val)  
            return True  
        logging.warn('The variable is already in queue')
        return False  
# Pop method to remove element  
    def remove_element(self):  
        if len(self.queue)>0:  
            logging.info("Removed the element")  
            return self.queue.pop()  
        logging.warn('The queue is empty')
        return ("Queue is Empty")  
  
que = Queue()  
que.add_element("January")  
que.add_element("February")  
que.add_element("March")  
que.add_element("April")  
  
print(que)  
print(que.remove_element())  
print(que.remove_element())