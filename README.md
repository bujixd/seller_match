# seller_match

## Overall

For each seller, find the matching buyers.  A match means the seller and buyer have at least one intersecting industry and at least one intersecting geography. All the results are ranked by score number.

## Arguments
this script support three different type of arguments. --all, --seller_id (seller_id), --seller_ids(array of seller_id sperate by ",")

## How to execute
python3 match_engine.py --all<br />
python3 match_engine.py --seller_id 1640fb77-135c-43d4-8196-835e07245683<br />
python3 match_engine.py --seller_id 1640fb77-135c-43d4-8196-835e07245683, 6372c203-f540-4208-8def-94edfc8257e8<br />

## Test Cases
- User enter invalid agruments<br />
  Return “option is not recognized”
- User enter invalid seller_id<br />
  Return “Seller id doesn’t exisit”

## Sample Result
Python match_engine.py –all <br />
'fd0c848f-35a1-4cac-a5a7-312f95045c23': 
[{'id': '69214e60-a21e-409b-8b20-a53d7610feb0','score': 20},
 {'id': '154a3c78-fd61-4c63-9edc-b630bb6746ce','score': 16},
…..], 
'fc216f2b-c3f0-467e-b78d-88dc391030df': 
[{'id': 'fe66ba21-59ff-4f81-b078-b19b14eb3e54','score': 40},
 {'id': '6bb9449e-f4a2-43db-8948-63dd81f34429','score': 36},
….]<br />

Python match_engine.py --seller_id 1640fb77-135c-43d4-8196-835e07245683<br />
[{'id': '0829cd31-55c1-4ffe-8471-f4ab31c5d466', 'score': 22},
 {'id': '781c4499-955d-44f8-897d-d49f20f50a6e', 'score': 22},
 {'id': 'ccae0885-d178-4050-a62e-164d6366ba8c', 'score': 22},
 {'id': 'f5546b49-c514-42a0-a6f7-acb77d9bd404', 'score': 20},
 {'id': '332cf22d-b85f-4f2b-9211-4068df4c4393', 'score': 18},
 {'id': '69214e60-a21e-409b-8b20-a53d7610feb0', 'score': 18},
 {'id': 'aaad2611-a321-4c3c-93a3-1cfc4380ea81', 'score': 18},
 {'id': 'd0c21ca5-80be-420f-818c-a6fad555ea07', 'score': 16},
 {'id': '154a3c78-fd61-4c63-9edc-b630bb6746ce', 'score': 16},
 {'id': '050130a0-3afa-4dc3-a0df-8302a64cb402', 'score': 14},
 {'id': 'd8cafbfb-7ad9-4530-b12d-641a1effe658', 'score': 14},
 {'id': '881e5df0-2cd4-4e4e-b6fc-96e1499326bb', 'score': 14},
 {'id': 'a3af8d60-9c70-4c1a-9e25-fc6107a11d76', 'score': 12},
 {'id': 'e110129c-dc4e-4452-ac4c-7a1cef95ad68', 'score': 12},
 {'id': '6bb9449e-f4a2-43db-8948-63dd81f34429', 'score': 12},
 {'id': '52424486-18a8-4591-a4f5-2306d778b3d8', 'score': 12},
 {'id': 'af592363-dfc2-4319-a406-f57463cd69ba', 'score': 12},
 {'id': '2fe2fd8c-3f9d-445e-966d-49b29b623a73', 'score': 12},
 {'id': '07d3e63e-3ad8-4d82-9938-c5621184e558', 'score': 12},
 {'id': '7fd73064-ea11-4e0a-946e-22a380e1ce1b', 'score': 12},
 {'id': '14ccffce-7c3b-4a42-b538-3c2186ee93e4', 'score': 12},
 {'id': '4189a815-985a-4f0f-8fae-7e418706a50e', 'score': 12},
 {'id': '640eb9fa-b151-4784-bdd1-e17c2edc7ff5', 'score': 10},
 {'id': '4e974f3b-0341-4e3a-ae7d-0fb21b7941de', 'score': 10},
 {'id': 'dd13e6ea-f6b5-4c1c-a78b-fa8f0c4e843d', 'score': 8},
 {'id': '58574613-3b53-47b0-973d-7aabe9185f28', 'score': 8},
 {'id': '28c86da0-a79d-4e79-bfaa-d2b5068ae407', 'score': 8},
 {'id': '06d11f70-e9ca-4309-8fac-d73b16a22fad', 'score': 8},
 {'id': 'f670f693-197e-4257-8371-a5fb0617337a', 'score': 8},
 {'id': '1b981033-744e-45c8-8537-1c2cdc1d1fbe', 'score': 8},
 {'id': '192b0944-f89d-48f4-8d24-8c61b2025c86', 'score': 8},
 {'id': '280cf327-00ef-4198-bb20-8cf12303791d', 'score': 8},
 {'id': '9c1d538b-ab79-4c69-96d2-ea0c0977fa24', 'score': 8},
 {'id': 'd03d8253-4682-437f-8c39-91f1dfdcc677', 'score': 8},
 {'id': '5ed9dad3-2cf6-4e72-b374-ad5b78fcac28', 'score': 8},
 {'id': '206e16a4-4e36-444c-bbe8-0ec952fec071', 'score': 6},
 {'id': '6d8d8ea3-58b7-4cbe-9383-1323d1a4637b', 'score': 6},
 {'id': 'f416af17-6635-4834-89d3-102623de9e23', 'score': 6},
 {'id': 'e233a711-ebac-436b-9201-238057670651', 'score': 4},
 {'id': '1e741809-cf36-4768-bd9e-27c80b30a4d3', 'score': 4},
 {'id': 'e8a8c7a6-68e1-4080-8dd5-7771f01d8f3c', 'score': 4},
 {'id': 'bf0ae34c-7f31-4d4b-8fcc-e9f5f093764d', 'score': 4},
 {'id': '9f01c38b-62e3-4326-bad0-f50221b2d1bf', 'score': 4},
 {'id': 'e1a494be-6016-4695-977b-243e8b2a0035', 'score': 4},
 {'id': '966d3c0d-b7b8-46ff-9033-0d3d6ec9d9a0', 'score': 4},
 {'id': 'fe66ba21-59ff-4f81-b078-b19b14eb3e54', 'score': 4},
 {'id': 'd259176e-3c4f-4a3e-ba07-3331d496e8d6', 'score': 4}]<br />

Python match_engine.py --seller_ids 1640fb77-135c-43d4-8196-835e07245683,6372c203-f540-4208-8def-94edfc8257e8<br />
[('1640fb77-135c-43d4-8196-835e07245683',
  [{'id': '0829cd31-55c1-4ffe-8471-f4ab31c5d466', 'score': 22},
   {'id': '781c4499-955d-44f8-897d-d49f20f50a6e', 'score': 22},
   {'id': 'ccae0885-d178-4050-a62e-164d6366ba8c', 'score': 22},
   {'id': 'f5546b49-c514-42a0-a6f7-acb77d9bd404', 'score': 20},
   {'id': '332cf22d-b85f-4f2b-9211-4068df4c4393', 'score': 18},
   {'id': '69214e60-a21e-409b-8b20-a53d7610feb0', 'score': 18},
   {'id': 'aaad2611-a321-4c3c-93a3-1cfc4380ea81', 'score': 18},
   {'id': 'd0c21ca5-80be-420f-818c-a6fad555ea07', 'score': 16},
   {'id': '154a3c78-fd61-4c63-9edc-b630bb6746ce', 'score': 16},
   {'id': '050130a0-3afa-4dc3-a0df-8302a64cb402', 'score': 14},
   {'id': 'd8cafbfb-7ad9-4530-b12d-641a1effe658', 'score': 14},
   {'id': '881e5df0-2cd4-4e4e-b6fc-96e1499326bb', 'score': 14},
   {'id': 'a3af8d60-9c70-4c1a-9e25-fc6107a11d76', 'score': 12},
   {'id': 'e110129c-dc4e-4452-ac4c-7a1cef95ad68', 'score': 12},
   {'id': '6bb9449e-f4a2-43db-8948-63dd81f34429', 'score': 12},
   {'id': '52424486-18a8-4591-a4f5-2306d778b3d8', 'score': 12},
   {'id': 'af592363-dfc2-4319-a406-f57463cd69ba', 'score': 12},
   {'id': '2fe2fd8c-3f9d-445e-966d-49b29b623a73', 'score': 12},
   {'id': '07d3e63e-3ad8-4d82-9938-c5621184e558', 'score': 12},
   {'id': '7fd73064-ea11-4e0a-946e-22a380e1ce1b', 'score': 12},
   {'id': '14ccffce-7c3b-4a42-b538-3c2186ee93e4', 'score': 12},
   {'id': '4189a815-985a-4f0f-8fae-7e418706a50e', 'score': 12},
   {'id': '640eb9fa-b151-4784-bdd1-e17c2edc7ff5', 'score': 10},
   {'id': '4e974f3b-0341-4e3a-ae7d-0fb21b7941de', 'score': 10},
   {'id': 'dd13e6ea-f6b5-4c1c-a78b-fa8f0c4e843d', 'score': 8},
   {'id': '58574613-3b53-47b0-973d-7aabe9185f28', 'score': 8},
   {'id': '28c86da0-a79d-4e79-bfaa-d2b5068ae407', 'score': 8},
   {'id': '06d11f70-e9ca-4309-8fac-d73b16a22fad', 'score': 8},
   {'id': 'f670f693-197e-4257-8371-a5fb0617337a', 'score': 8},
   {'id': '1b981033-744e-45c8-8537-1c2cdc1d1fbe', 'score': 8},
   {'id': '192b0944-f89d-48f4-8d24-8c61b2025c86', 'score': 8},
   {'id': '280cf327-00ef-4198-bb20-8cf12303791d', 'score': 8},
   {'id': '9c1d538b-ab79-4c69-96d2-ea0c0977fa24', 'score': 8},
   {'id': 'd03d8253-4682-437f-8c39-91f1dfdcc677', 'score': 8},
   {'id': '5ed9dad3-2cf6-4e72-b374-ad5b78fcac28', 'score': 8},
   {'id': '206e16a4-4e36-444c-bbe8-0ec952fec071', 'score': 6},
   {'id': '6d8d8ea3-58b7-4cbe-9383-1323d1a4637b', 'score': 6},
   {'id': 'f416af17-6635-4834-89d3-102623de9e23', 'score': 6},
   {'id': 'e233a711-ebac-436b-9201-238057670651', 'score': 4},
   {'id': '1e741809-cf36-4768-bd9e-27c80b30a4d3', 'score': 4},
   {'id': 'e8a8c7a6-68e1-4080-8dd5-7771f01d8f3c', 'score': 4},
   {'id': 'bf0ae34c-7f31-4d4b-8fcc-e9f5f093764d', 'score': 4},
   {'id': '9f01c38b-62e3-4326-bad0-f50221b2d1bf', 'score': 4},
   {'id': 'e1a494be-6016-4695-977b-243e8b2a0035', 'score': 4},
   {'id': '966d3c0d-b7b8-46ff-9033-0d3d6ec9d9a0', 'score': 4},
   {'id': 'fe66ba21-59ff-4f81-b078-b19b14eb3e54', 'score': 4},
   {'id': 'd259176e-3c4f-4a3e-ba07-3331d496e8d6', 'score': 4}]),
 ('6372c203-f540-4208-8def-94edfc8257e8',
  [{'id': '640eb9fa-b151-4784-bdd1-e17c2edc7ff5', 'score': 22},
   {'id': 'e110129c-dc4e-4452-ac4c-7a1cef95ad68', 'score': 18},
   {'id': '154a3c78-fd61-4c63-9edc-b630bb6746ce', 'score': 18},
   {'id': '050130a0-3afa-4dc3-a0df-8302a64cb402', 'score': 18},
   {'id': '69214e60-a21e-409b-8b20-a53d7610feb0', 'score': 18},
   {'id': 'f5546b49-c514-42a0-a6f7-acb77d9bd404', 'score': 14},
   {'id': 'd0c21ca5-80be-420f-818c-a6fad555ea07', 'score': 14},
   {'id': '0829cd31-55c1-4ffe-8471-f4ab31c5d466', 'score': 14},
   {'id': '14ccffce-7c3b-4a42-b538-3c2186ee93e4', 'score': 14},
   {'id': '28c86da0-a79d-4e79-bfaa-d2b5068ae407', 'score': 12},
   {'id': 'ccae0885-d178-4050-a62e-164d6366ba8c', 'score': 10},
   {'id': '206e16a4-4e36-444c-bbe8-0ec952fec071', 'score': 10},
   {'id': 'f416af17-6635-4834-89d3-102623de9e23', 'score': 10},
   {'id': '52424486-18a8-4591-a4f5-2306d778b3d8', 'score': 10},
   {'id': 'e1a494be-6016-4695-977b-243e8b2a0035', 'score': 10},
   {'id': 'dd13e6ea-f6b5-4c1c-a78b-fa8f0c4e843d', 'score': 8},
   {'id': '07d3e63e-3ad8-4d82-9938-c5621184e558', 'score': 8},
   {'id': '9c1d538b-ab79-4c69-96d2-ea0c0977fa24', 'score': 8},
   {'id': 'd8cafbfb-7ad9-4530-b12d-641a1effe658', 'score': 8},
   {'id': '9f01c38b-62e3-4326-bad0-f50221b2d1bf', 'score': 8},
   {'id': '881e5df0-2cd4-4e4e-b6fc-96e1499326bb', 'score': 8},
   {'id': '332cf22d-b85f-4f2b-9211-4068df4c4393', 'score': 6},
   {'id': '781c4499-955d-44f8-897d-d49f20f50a6e', 'score': 6},
   {'id': '6d8d8ea3-58b7-4cbe-9383-1323d1a4637b', 'score': 6},
   {'id': 'bf0ae34c-7f31-4d4b-8fcc-e9f5f093764d', 'score': 6},
   {'id': 'aaad2611-a321-4c3c-93a3-1cfc4380ea81', 'score': 6},
   {'id': '7fd73064-ea11-4e0a-946e-22a380e1ce1b', 'score': 6},
   {'id': '3626e8a4-8b25-4671-8a24-0061dd465611', 'score': 6},
   {'id': 'd03d8253-4682-437f-8c39-91f1dfdcc677', 'score': 6},
   {'id': '4189a815-985a-4f0f-8fae-7e418706a50e', 'score': 4},
   {'id': '280cf327-00ef-4198-bb20-8cf12303791d', 'score': 4},
   {'id': '2fe2fd8c-3f9d-445e-966d-49b29b623a73', 'score': 4},
   {'id': '1b981033-744e-45c8-8537-1c2cdc1d1fbe', 'score': 4},
   {'id': '06d11f70-e9ca-4309-8fac-d73b16a22fad', 'score': 4},
   {'id': 'fe66ba21-59ff-4f81-b078-b19b14eb3e54', 'score': 4},
   {'id': '4e974f3b-0341-4e3a-ae7d-0fb21b7941de', 'score': 4},
   {'id': '58574613-3b53-47b0-973d-7aabe9185f28', 'score': 4},
   {'id': 'a3af8d60-9c70-4c1a-9e25-fc6107a11d76', 'score': 4},
   {'id': '192b0944-f89d-48f4-8d24-8c61b2025c86', 'score': 4},
   {'id': '5ed9dad3-2cf6-4e72-b374-ad5b78fcac28', 'score': 4}])]<br />

## Ranking Method
For every buyer and seller. Each matched geo_id scores 4 point and each matched industry_id scores 6 points.
At the end, rank the result by points.
