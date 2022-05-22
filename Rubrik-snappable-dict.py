# Design and implement a key-value store library that support snapshots
#
# Your data structure should expose below APIs:
# put(key, value) # upsert a key-value pair
# delete(key) # delete a key
# takeSnapshot() -> Snapshot # take a snapshot of the current stored data
# deleteSnapshot(snapshot) # delete a snapshot
# get(key) # get value from data structure
# getFromSnapshot(key, snapshot) # get value from a snapshot
#
# Example:
# put(k1, v1)
# put(k2, v2)
# put(k3, v3)
# takeSnapshot-> snap1{k1-> v1, k2-> v2, k3-> v3}
# getFromSnapshot(k1, snap1)-> v1
# put(k1, v4)
# get(k1) -> v4
# delete(k3)
# takeSnapshot-> snap2{k1-> v4, k2-> v2}
# getFromSnapshot(k1, snap2)-> v4
# getFromSnapshot(k1, snap1) -> v1
# getFromSnapshot(k3, snap2) -> Key k3 not found
# getFromSnapshot(k3, snap1) -> v3
# deleteSnapshot(snap1)
# getFromSnapshot(k1, snap1) -> Snapshot snap1 not found
