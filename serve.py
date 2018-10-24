import model as model

def get_model_api():
	model.build()

	def model_api(input_data):
		s = [int(i) for i in input_data.split()]
		raw_value_one = s[0]
		raw_value_two = s[1]
		raw_value_three = s[2]
		prediction = model.predict(raw_value_one, raw_value_two, raw_value_three)

		return prediction

	return model_api