
def analyzePeaks(tp):
      
      count = 0
      values = ()
      indexes = ()

      for j in range(1, len(tp)-1):
            if tp[j] > tp[j-1] and tp[j] > tp[j+1]:
                  count += 1
                  values += (tp[j],)
                  indexes += (j,)

      return count, values, indexes


t = (2, 4, 87, 34, 23)

cnt, vals, idxs = analyzePeaks(t)

print("tuple:", t)
print("peak count:", cnt)
print("peak vals:", vals)
print("peak index:", idxs)