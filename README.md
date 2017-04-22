# seller_match

## Overall

For each seller, find the matching buyers.  A match means the seller and buyer have at least one intersecting industry and at least one intersecting geography. All the results are ranked by score number.

## Arguments
this script support three different type of arguments. --all, --seller_id (seller_id), --seller_ids(array of seller_id sperate by ",")

## How to execute
python3 match_engine.py --all<br />
python3 match_engine.py --seller_id 1640fb77-135c-43d4-8196-835e07245683<br />
python3 match_engine.py --seller_id 1640fb77-135c-43d4-8196-835e07245683, 6372c203-f540-4208-8def-94edfc8257e8<br />

