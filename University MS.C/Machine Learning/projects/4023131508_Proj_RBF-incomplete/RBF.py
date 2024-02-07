import numpy as np
from sklearn.cluster import KMeans
import math

class RBF:
	def __init__(self,inputs,no_clusters,outputs,learning_rate):
		self.inputs = inputs
		self.no_clusters = no_clusters
		self.weight = self.cal_weights()
		self.outputs = outputs
		self.f_out = 0
		self.centers = []
		self.sigma = 0
		self.learning_rate = learning_rate
		self.m_rbf = []


	def guassian(self,x, mo)->float:
		# print(self.sigma)
		# print(self.sigma**2)
		# print((2*(self.sigma**2)))
		return math.exp(-(np.linalg.norm(x-mo)**2)/(2*(self.sigma**2)))


	def cal_weights(self)->[]:
		weight = np.random.uniform(0,1,size=(self.no_clusters,1))
		return weight


	def feedforward(self,input):
		self.m_rbf = np.array([])
		for j in range(len(self.centers)):
			self.m_rbf=np.append(self.m_rbf,self.guassian(input,self.centers[j]))

		self.m_rbf = self.m_rbf.reshape(len(self.m_rbf),1)
		self.f_out=np.dot(self.m_rbf.T,self.weight)[0][0]
		if self.f_out == np.inf:
			print()


	def backward(self,f_d):
		delta = f_d - self.f_out
		self.weight += self.learning_rate*delta*self.m_rbf




	def train(self,epoch, sigma = None):
		kmeans = KMeans(n_clusters=self.no_clusters, random_state=0, n_init="auto").fit(self.inputs)
		self.centers = kmeans.cluster_centers_
		if sigma != None:
			self.sigma = sigma
		else:
			self.sigma = np.max([np.abs(np.linalg.norm(cent1 - cent2)) for cent1 in self.centers for cent2 in self.centers])/math.sqrt(2*self.no_clusters)
		for _ in range(epoch):
			for i in range(len(self.inputs)):
				self.feedforward(self.inputs[i])
				# if i == 0:
					# print(self.inputs[i])
					# print(f"{self.f_out}, desired = {self.outputs[i][0]}")
					# print("-----")
				self.backward(self.outputs[i][0])



	def test(self,inputs,outputs):
		true=0
		for i in range(len(inputs)):
			self.feedforward(inputs[i])

			if abs(self.f_out - outputs[i][0])<=150:
				true +=1

		return true/len(inputs)*100