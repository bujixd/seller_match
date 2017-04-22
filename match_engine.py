'''
Created on Apr 21, 2017

@author: zhichen
'''
import json
from pprint import pprint
from collections import defaultdict
import getopt, sys

class BuyersWithScore(object):
    
    def __init__(self, buyer_id, score):
        self.buyer_id = buyer_id
        self.score = score


class MatchBuyerExecutor(object):
    
    industry_match = 6
    geo_match = 4
    


    def generate_result(self):
        json_file='sample_data.json'
        json_data=open(json_file)
        data = json.load(json_data)
        
        self.geo_indstury_ids=defaultdict(dict)

        # parse data into a dict
        # key is geo or industry id
        # value is lists of seller_id or buyer_id that related to this geo or industry id
        # e.g. 
        
        for x in data:
            MatchBuyerExecutor.json_decode(self, x, True)
            MatchBuyerExecutor.json_decode(self, x, False)
        
        
        results = defaultdict(list)
        
        for _, buyer_seller_ids in self.geo_indstury_ids.items():
            for (buyer_score, seller_id) in [(x, y) for x in buyer_seller_ids['buyers'] for y in buyer_seller_ids['seller']]:
                for i in range(len(results[seller_id])):
                    if buyer_score.buyer_id in results[seller_id][i]['id']:
                        results[seller_id][i]['score'] += buyer_score.score 
                        break
                else:
                    results[seller_id].append({'id' : buyer_score.buyer_id, 'score' : buyer_score.score})
        
        
                
        self.result = results
        MatchBuyerExecutor.rank_result(self)
    
    def json_decode(self, data, is_geo):
        
        id = 'geography_ids' if is_geo == True else 'industry_ids'
        score = MatchBuyerExecutor.geo_match if is_geo == True else MatchBuyerExecutor.industry_match
        
        for geo_indstury_id in data['details'][id]:
            if geo_indstury_id not in self.geo_indstury_ids:
                self.geo_indstury_ids[geo_indstury_id] = {}
                self.geo_indstury_ids[geo_indstury_id]['buyers'] = []
                self.geo_indstury_ids[geo_indstury_id]['seller'] = []
                    
            if data['type'] == 'buyer':  
                self.geo_indstury_ids[geo_indstury_id]['buyers'].append(BuyersWithScore(data['id'], score))
            else:
                self.geo_indstury_ids[geo_indstury_id]['seller'].append(data['id'])
    
    
    def rank_result(self):
        for seller_id in self.result:
            self.result[seller_id].sort(key=lambda k: k['score'], reverse=True)

    def get_results_all(self):
        return self.result
    
    def get_result_by_seller_id(self, seller_id):
        if seller_id in self.result:
            return self.result[seller_id]
        else:
            return 'seller id doesnt exist'
    
    def get_result_by_seller_ids(self, seller_ids):
        res = []
        
        for seller_id in seller_ids:
            if seller_id in self.result:
                res.append((seller_id, self.result[seller_id]))
        
        if not res:
            return 'none of the seller_ids exist'
        else:
            return res

def main():
    try:
        opts,_ = getopt.getopt(sys.argv[1:],"", ["all", "seller_id=", "seller_ids="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        sys.exit(2)
    
    match_buyer = MatchBuyerExecutor()
    match_buyer.generate_result()
    for opt, arg in opts:
        if opt in ("--all"):
            pprint(match_buyer.get_results_all())
        elif opt in ("--seller_id"):
            pprint(match_buyer.get_result_by_seller_id(arg))
        elif opt in ("--seller_ids"):
            pprint(match_buyer.get_result_by_seller_ids(arg.split(',')))
        else:
            assert False, "unhandled option"
    # ...

if __name__ == '__main__':
    main()
