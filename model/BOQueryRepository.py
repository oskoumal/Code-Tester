
from model.Query import Query

class BOQueryRepository(object):
	"""Defines graph database queries for Buffer-Overflow type of vulnerabilities and access methods for their usage"""

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY1 = Query(
		# Number of query
		"1", 

		# Name
		"FABIAN'S VLC QUERY I libssh bug malloc", 

		# Query code
		""" 

		getCallsTo("malloc").ithArguments("0")
		.sideEffect { cnt = it.code }
		.match { it.type == "AdditiveExpression" }.statements()
		.out("REACHES")
		.match { it.type == "CallExpression" && it.code.startsWith("memcpy") }.ithArguments("2")
		.filter { it.code != cnt }
		.match { it.type == "AdditiveExpression" }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW in connection with MEMCPY and MALLOC functions, 
		targeting possible wrongdoings in additive expression calculations in their arguments.
		

		""",

		# Description of query usage
		"""

		query usage


		""")

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY2 = Query(
		# Number of query
		"2", 

		# Name
		"FABIAN'S VLC QUERY I libssh bug calloc", 

		# Query code
		""" 

		getCallsTo("calloc").ithArguments("0")
		.sideEffect { cnt = it.code }
		.match { it.type == "AdditiveExpression" }.statements()
		.out("REACHES")
		.match { it.type == "CallExpression" && it.code.startsWith("memcpy") }.ithArguments("2")
		.filter { it.code != cnt }
		.match { it.type == "AdditiveExpression" }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW in connection with MEMCPY and CALLOC functions, 
		targeting possible wrongdoings in additive expression calculations in their arguments.
		

		""",

		# Description of query usage
		"""

		query usage


		""")

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY3 = Query(
		# Number of query
		"3", 

		# Name
		"VLAD'S IMPROVED FABIAN'S VLC I QUERY malloc", 

		# Query code
		""" 

		getCallsTo("malloc").ithArguments("0")
		.sideEffect { expression = it.code }
		.filter { it.match { it.type == "Identifier" }.count() == 1 }
		.sideEffect { variable = it.match { it.type == "Identifier" }.code }
		.statements().out("REACHES")
		.match { it.type == "CallExpression" && it.code.startsWith("memcpy") }.ithArguments("2")
		.filter { it.code != expression }
		.filter { it.match { it.type == "Identifier" }.count() == 1 }
		.filter { it.match { it.type == "Identifier" }.code.toList()[0] == variable.toList()[0] }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW in connection with MEMCPY and MALLOC functions, slightly 
		other searching approach than previous queries.

		""",

		# Description of query usage
		"""

		query usage


		""")

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY4 = Query(
		# Number of query
		"4", 

		# Name
		"VLAD'S IMPROVED FABIAN'S VLC I QUERY calloc", 

		# Query code
		""" 

		getCallsTo("calloc").ithArguments("0")
		.sideEffect { expression = it.code }
		.filter { it.match { it.type == "Identifier" }.count() == 1 }
		.sideEffect { variable = it.match { it.type == "Identifier" }.code }
		.statements().out("REACHES")
		.match { it.type == "CallExpression" && it.code.startsWith("memcpy") }.ithArguments("2")
		.filter { it.code != expression }
		.filter { it.match { it.type == "Identifier" }.count() == 1 }
		.filter { it.match { it.type == "Identifier" }.code.toList()[0] == variable.toList()[0] }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW in connection with MEMCPY and CALLOC functions, slightly 
		other searching approach than previous queries.

		""",

		# Description of query usage
		"""

		query usage


		""")

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY5 = Query(
		# Number of query
		"5", 

		# Name
		"REWRITTEN FABIAN'S VLC QUERY II truncations in allocations  malloc", 

		# Query code
		""" 

		getCallsTo("malloc").ithArguments("0")
		.sideEffect { expression = it.code.toList()[0] }
		.statements()
		.in("REACHES")
		.filter{ it.code.contains("int64_t") }
		.filter{ it.code.contains(expression) }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW caused by truncations in allocations, in connection with
		the potentially dangerous int64_t type. 

		""",

		# Description of query usage
		"""

		query usage


		""")

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY6 = Query(
		# Number of query
		"6", 

		# Name
		"REWRITTEN FABIAN'S VLC QUERY II truncations in allocations  calloc", 

		# Query code
		""" 

		getCallsTo("calloc").ithArguments("0")
		.sideEffect { expression = it.code.toList()[0] }
		.statements()
		.in("REACHES")
		.filter{ it.code.contains("int64_t") }
		.filter{ it.code.contains(expression) }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW caused by truncations in allocations, in connection with
		the potentially dangerous int64_t type. 

		""",

		# Description of query usage
		"""

		query usage


		""")

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY7 = Query(
		# Number of query
		"7", 

		# Name
		"MODIFIED FABIAN'S VLC QUERY I libssh bug malloc for strcpy", 

		# Query code
		""" 

		getCallsTo("malloc").ithArguments("0")
		.sideEffect { cnt = it.code }
		.match { it.type == "AdditiveExpression" }
		.statements()
		.out("REACHES")
		.match { it.type == "CallExpression" && it.code.startsWith("strcpy") }.ithArguments("1")
		.filter { it.code != cnt }
		.match { it.type == "AdditiveExpression" }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW in connection with STRCPY and MALLOC functions, 
		targeting possible wrongdoings in additive expression calculations in their arguments.
		

		""",

		# Description of query usage
		"""

		query usage


		""")

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY8 = Query(
		# Number of query
		"8", 

		# Name
		"MODIFIED FABIAN'S VLC QUERY I libssh bug calloc for strcpy", 

		# Query code
		""" 

		getCallsTo("calloc").ithArguments("0")
		.sideEffect { cnt = it.code }
		.match { it.type == "AdditiveExpression" }.statements()
		.out("REACHES")
		.match { it.type == "CallExpression" && it.code.startsWith("strcpy") }.ithArguments("2")
		.filter { it.code != cnt }
		.match { it.type == "AdditiveExpression" }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW in connection with STRCPY and CALLOC functions, 
		targeting possible wrongdoings in additive expression calculations in their arguments.
		

		""",

		# Description of query usage
		"""

		query usage


		""")

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY9 = Query(
		# Number of query
		"9", 

		# Name
		"MODIFIED VLAD'S IMPROVED FABIAN'S VLC QUERY malloc strcpy", 

		# Query code
		""" 

		getCallsTo("malloc").ithArguments("0")
		.sideEffect { expression = it.code }
		.filter { it.match { it.type == "Identifier" }.count() == 1 }
		.sideEffect { variable = it.match { it.type == "Identifier" }.code }
		.statements()
		.out("REACHES")
		.match { it.type == "CallExpression" && it.code.startsWith("strcpy") }.ithArguments("1")
		.filter { it.code != expression }
		.filter { it.match { it.type == "Identifier" }.count() == 1 }
		.filter { it.match { it.type == "Identifier" }.code.toList()[0] == variable.toList()[0] }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW in connection with STRCPY and MALLOC functions, slightly 
		other searching approach than previous queries.

		""",

		# Description of query usage
		"""

		query usage


		""")

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY10 = Query(
		# Number of query
		"10", 

		# Name
		"MODIFIED VLAD'S IMPROVED FABIAN'S VLC QUERY calloc strcpy", 

		# Query code
		""" 

		getCallsTo("calloc").ithArguments("0")
		.sideEffect { expression = it.code }
		.filter { it.match { it.type == "Identifier" }.count() == 1 }
		.sideEffect { variable = it.match { it.type == "Identifier" }.code }
		.statements()
		.out("REACHES")
		.match { it.type == "CallExpression" && it.code.startsWith("strcpy") }.ithArguments("1")
		.filter { it.code != expression }
		.filter { it.match { it.type == "Identifier" }.count() == 1 }
		.filter { it.match { it.type == "Identifier" }.code.toList()[0] == variable.toList()[0] }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Generalized query searching for BUFFER-OVERFLOW in connection with STRCPY and CALLOC functions, slightly 
		other searching approach than previous queries.

		""",
		# Description of query usage
		"""

		query usage


		""")


	QUERYLIST = [QUERY1, QUERY2, QUERY3, QUERY4, QUERY5, QUERY6, QUERY7, QUERY8, QUERY9, QUERY10]

	def getQueryList(self):
		return BOQueryRepository.QUERYLIST







