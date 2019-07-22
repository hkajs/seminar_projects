gen = 1
indiv = 1

fullgen:
	make fullrun gen=${gen}
	make fullrun gen=${gen}
	make fullrun gen=${gen}
	make fullrun gen=${gen}
	make fullrun gen=${gen}
	python flattenFitness.py ${gen}

fullrun:
	make onerun gen=${gen} indiv=1
	make onerun gen=${gen} indiv=2
	make onerun gen=${gen} indiv=3
	make onerun gen=${gen} indiv=4
	make onerun gen=${gen} indiv=5
	make onerun gen=${gen} indiv=6
	make onerun gen=${gen} indiv=7
	make onerun gen=${gen} indiv=8
	make onerun gen=${gen} indiv=9
	make onerun gen=${gen} indiv=10

onerun:
	python serverbot_fitness.py & run python auctionclient_genetic.py ${gen} ${indiv} & run python auctionclient_aggro.py & run python auctionclient_blocker.py