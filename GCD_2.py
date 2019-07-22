#this is the secound way to find out the GCD no. 
def gcd(m,n):
  #let suppose m>=n
  if m<n:
    #we just simply swap the no. if it is wrong.
    (m,n)=(n,m)
    
  if (m%n)==0:
    return (n)
  else: 
    diff =m-n
    return (gcd(max(n,diff),min(n,diff)))
