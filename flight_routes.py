our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Finding destinations both travel to 
same_destination = our_routes.intersection(competitor_routes)
print(f"Both airlines travel to {same_destination}")

#Finding our_routes unique airlines
uniqie_routes = our_routes.difference(competitor_routes)
print(f"Our airlines provide{uniqie_routes} while our competitor does not")

#Finding destinations niether airlines share
no_share_routes = our_routes.symmetric_difference(competitor_routes)
print(f"Niether airline shares {no_share_routes}")