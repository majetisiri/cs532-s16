def sim_pearson(pref,p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in pref[p1]: 
    if item in pref[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
    
  sum1 = 0
  for it in si:
	sum1 =  sum1 + int(pref[p1][it])

  sum2 = 0
  for it in si:
	sum2 =  sum2 + int(pref[p2][it])

  sum1Sq = 0
  for it in si:
	sum1Sq =  sum1Sq + pow(int(pref[p1][it]),2)
  
  sum2Sq = 0
  for it in si:
	sum2Sq =  sum2Sq + pow(int(pref[p2][it]),2)

  
  pSum = 0  
  for it in si:
	pSum =  pSum + ( int(pref[p2][it]) * int(pref[p1][it]) )
	
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r