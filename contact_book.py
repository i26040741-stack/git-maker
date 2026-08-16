class city:
  def __init__(self,country,city,fouded,population,mayor,landmarks):

   self.country = country
   self.city = city
   self.founded = fouded 
   self.population = population
   self.mayor = mayor
   self.landmarks = landmarks

  def describe(self):
    print(f"City: {self.city}")
    print(f"Founded: {self.founded}")
    print(f"Mayor: {self.mayor}")
    print("Key Landmarks: ")
    for i in self.landmarks:
      print(f"- {i}")
    print('_' * 30) 



Kuala_Lumpur = city(country = "Malaysia",
city = 'Kuala Lumpur (Garden City of Lights)',
fouded = "1857",
population = "8,420,000",
mayor = 'Mainunah Mohd Sharif',
landmarks = 
['Petronas Twin Towers',
'KL Tower',
'Batu Caves'])
dream_city = city(country = "Japan"
,city = 'Tokyo (The Big Mikan)'
,fouded = "1603",
population = "14,090,000",
mayor = 'Yuriko Koike',
landmarks = ['Tokyo Skytree'
,'Senso-ji Temple',
'Shibuya Crossing'])
Kuala_Lumpur.describe()
dream_city.describe()