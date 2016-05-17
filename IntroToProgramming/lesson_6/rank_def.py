
#outlinks = [list of links on page]
#inlinks = [list of links to page]
#d = 0.8
#N = number of pages

#rank(0, url) -> 1/N
#rank(t, url) -> d * sum_inlinks(rank(t - 1, p)/outlinks[p]) + (1 - d)/N




rank(0,url) = 1/npages
rank(t,url) = (1-d)/npages + sum_inlinks(d * rank(t - 1, p) / outlinks

ranks -> ranks at time t-1
newranks -> ranks at time t
