'''
    gia ka8e pi8ani apokrisi (i opoia vrisketai sto telos ka8e dianismatos dedomenwn) exw kai enan pinaka apo counters
    dld to counters einai ena dictionary to opoio lamvanei mia apokrisi kai se autin antistoixei enan pinaka
    o opoios krataei metrites gia ka8e attribute (pinakes ousiastika). twra omws ka8e attribute mporei na exei
    polles dinates times, opote ka8e dia8esimi 8esi t pinaka gia tn filo3enisi tou metriti gia to attribute stn 8esi auti,
    einai dictionary pou krataei tous metrites gia ka8e diaforetiki timi tou attribute
    '''


class NaiveBayes:

    def __init__(self):
        self.c_counter = None
        self.feature_values = None
        self.num_in_each_category = None

    def train(self, data, categories, feature_values):
        self.feature_values = feature_values
        '''
        categories ---> a list of the possible categories
        '''
        c_counter = dict.fromkeys(categories, [dict.fromkeys(feature, 0) for feature in self.feature_values])

        self.num_in_each_category = dict.fromkeys(categories, 0)
        for d in data:
            for i in range(len(d)-1):
                # d[-1] ---> the category
                # i ---> the feature number
                # d[i] ---> the value of feature i for the data 'd'
                c_counter.get(d[-1])[i][d[i]] += 1
                self.num_in_each_category[d[-1]] += 1

        self.c_counter = c_counter

    def extract_feature_values(self, data):
        dataT = [[]] * len(data[0])
        for d in data:
            for i in range(len(d)):
                if d[i] not in dataT[i]:
                    dataT[i].append(d[i])
        return dataT

    def set_feature_values(self, f_v):
        self.feature_values = f_v

    def response(self, d):
        # ipologismos "pi8anotitnw"

        c_max = 0
        answer = 0

        num_of_data = 0
        for c in self.num_in_each_category.keys():
            num_of_data += self.num_in_each_category.get(c)

        for c in self.c_counter.keys():
            current_product = 1
            for i in range(0, len(d)):
                N = self.num_in_each_category.get(c) + len(self.feature_values[i])
                current_product *= (self.c_counter.get(c)[i].get(d[i]) + 1)/N

            prob = current_product * self.num_in_each_category.get(c)/num_of_data
            if prob > c_max:
                c_max = prob
                answer = c

        return answer

    def response_all(self, data):
        responses = []
        for d in data:
            responses.append(self.response(d))
        return responses
