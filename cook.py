class Restaurant:
	"""A simple attempt at a resturant"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize name and cuisine"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_resturant(self):
		"""Display a summery of the resturant"""
		msg = f"{self.restaurant_name} serves mainly {self.cuisine_type} food."
		print(f"\n{msg}")

	def open_resturant(self):
		"""Give a message that the resturant is now open"""
		msg = f"{self.restaurant_name} is now open for buisness!!!"
		print(f"\n{msg}")

	def set_number_served(self, number_served):
		"""Allow user to set the number of customers served."""
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		"""Increment the number of customers who've all ready been served"""
		self.number_served += additional_served

		



# Now make a instance class for the resturant
#restaurant = Restaurant("the mean queen", "pizza")
#restaurant.describe_resturant()

#print(f"\nNumber served: {restaurant.number_served}")
#restaurant.number_served = 500
#print(f"Number served: {restaurant.number_served}")

#restaurant.set_number_served(860)
#print(f"Number served: {restaurant.number_served}")

#restaurant.increment_number_served(1234)
#print(f"Number served: {restaurant.number_served}")