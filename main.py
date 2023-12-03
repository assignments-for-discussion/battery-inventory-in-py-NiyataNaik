
def count_batteries_by_health(present_capacities):
  health_dict= {"healthy": 0,"exchange": 0,"failed": 0}
  
  for present_capacity in present_capacities:
    rated_capacity=120
    soh=100 * present_capacity/rated_capacity

    if soh>80:
      health_dict["healthy"]+=1
    elif soh>=62 and soh<=80:
      health_dict["exchange"]+=1
    else:
      health_dict["failed"]+=1
  return health_dict

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113,80, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 4)
  assert(counts["failed"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
