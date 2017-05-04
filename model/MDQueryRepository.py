
from model.Query import Query

class MDQueryRepository(object):
	"""Defines graph database queries for Memory disclosure type of vulnerabilities and access methods for their usage"""

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY1 = Query(
		# Number of query
		"1", 

		# Name
		"MODIFIED FABIAN'S LINUX QUERY II memcpy heartbleed ", 

		# Query code
		""" 

		import java.util.regex.Pattern;
		getArguments('memcpy', '2')
		.filter{ !it.argToCall().toList()[0].code.matches('.*(sizeof|min).*') }
		.sideEffect{ argument = it.code; }
		.sideEffect{ sId = it.statements().toList()[0].id; }
		.unsanitized(
		{ it, s -> it._().or(
			_().isCheck('.*' + Pattern.quote(argument) + '.*'),
			_().codeContains('.*lloc.*' + Pattern.quote(argument) + '.*'),
			_().codeContains('.*min.*'))})
		.filter{ it.id != sId }
		.filter{ !it.code.contains("lloc") }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Very broad search taint-style query, GREP-LIKE approach, targeting for unsanitized
		arguments of MEMCPY function.
	

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
		"HEAVILY MODIFIED FABIAN'S LINUX QUERY II  memcpy  -orezavani", 

		# Query code
		""" 

		import java.util.regex.Pattern;
		getCallsTo("memcpy")
		.as('calls')
		.ithArguments("2")
		.filter{ !it.argToCall().toList()[0].code.matches('.*(sizeof|min).*') }
		.sideEffect{ argument = it.code; }
		.sideEffect{ sId = it.statements().toList()[0].id; }
		.unsanitized(
		{ it, s -> it._().or(
			_().isCheck('.*' + Pattern.quote(argument) + '.*'),
			_().codeContains('.*lloc.*' + Pattern.quote(argument) + '.*'),
			_().codeContains('.*min.*'))})
		.filter{ it.id != sId }
		.filter{ !it.code.contains("lloc") }
		.dedup()

		.as('results')
		.back('calls')

		.ithArguments("2")
		.filter{ !it.argToCall().toList()[0].code.matches('.*(sizeof|min).*') }
		.sideEffect{ paramName = 'len(gth)?'; }
		.filter{ it.code.contains("len") }
		.sideEffect{ sIdd = it.statements().toList()[0].id; }
		.unsanitized(
		{ it, s -> it._().or(
			_().isCheck('.*' + Pattern.quote(paramName) + '.*'),
			_().codeContains('.*lloc.*' + Pattern.quote(paramName) + '.*'),
			_().codeContains('.*max.*'),
			_().codeContains('.*min.*'))})
		.filter{ it.id != sIdd }
		.filter{ !it.code.contains("lloc") }
		.dedup()

		.except('results')
		.locations()

		""",

		# General description
		"""

		More targeted broad search using 'len' as target argument, taint-style query, 
		GREP-LIKE approach, targeting for unsanitized arguments of MEMCPY function.

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
		"Overflow in static char array allocations memcpy query", 

		# Query code
		""" 

		getArguments('memcpy', '2')
		.sideEffect{ argument = it.code; }
		.filter{ it.code.contains("len") }
		.statements()
		.in("REACHES")
		.filter{ it.code.contains("char") }
		.match { it.type == "IdentifierDeclStatement" }
		.filter{ it.code.contains(argument) }
		.filter{ !it.code.contains("*") }
		.filter{ it.code.contains("[") }
		.dedup()
		.locations()

		""",

		# General description
		"""

		More targeted search using 'len' as target argument, taint-style query, 
		GREP-LIKE approach. Searches for specific bug - overflow in static char array allocations.

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
		"MODIFIED FABIAN'S LINUX QUERY II strcpy heartbleed", 

		# Query code
		""" 

		import java.util.regex.Pattern;
		getArguments('strcpy', '1')
		.filter{ !it.argToCall().toList()[0].code.matches('.*(sizeof|min).*') }
		.sideEffect{ argument = it.code; }
		.sideEffect{ sId = it.statements().toList()[0].id; }
		.unsanitized(
		{ it, s -> it._().or(
			_().isCheck('.*' + Pattern.quote(argument) + '.*'),
			_().codeContains('.*lloc.*' + Pattern.quote(argument) + '.*'),
			_().codeContains('.*min.*'))})
		.filter{ it.id != sId }
		.filter{ !it.code.contains("lloc") }
		.dedup()
		.locations()

		""",

		# General description
		"""

		Very broad search taint-style query, GREP-LIKE approach, targeting for unsanitized
		arguments of STRCPY function.

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
		"MODIFIED FABIAN LINUX QUERY II  more targeted broad search using 'len' as target argument STRCPY  taint-style query   -orezavani", 

		# Query code
		""" 

		import java.util.regex.Pattern;
		getArguments('strcpy', '1')
		.filter{ !it.argToCall().toList()[0].code.matches('.*(sizeof|min).*') }
		.sideEffect{ paramName = 'len(gth)?'; }
		.filter{ it.code.contains("len") }
		.sideEffect{ sId = it.statements().toList()[0].id; }
		.unsanitized(
		{ it, s -> it._().or(
			_().isCheck('.*' + Pattern.quote(paramName) + '.*'),
			_().codeContains('.*lloc.*' + Pattern.quote(paramName) + '.*'),
			_().codeContains('.*max.*'),
			_().codeContains('.*min.*'))})
		.filter{ it.id != sId }
		.filter{ !it.code.contains("lloc") }
		.dedup()
		.locations()

		""",

		# General description
		"""

		More targeted broad search using 'len' as target argument, taint-style query, 
		GREP-LIKE approach, targeting for unsanitized arguments of MEMCPY function.

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
		"Overflow in static char array allocations strcpy query", 

		# Query code
		""" 

		getArguments('strcpy', '1')
		.sideEffect{ argument = it.code; }
		.filter{ it.code.contains("len") }
		.statements()
		.in("REACHES")
		.filter{ it.code.contains("char") }
		.match { it.type == "IdentifierDeclStatement" }
		.filter{ it.code.contains(argument) }
		.filter{ !it.code.contains("*") }
		.filter{ it.code.contains("[") }
		.dedup()
		.locations()


		""",

		# General description
		"""

		More targeted search using 'len' as target argument, taint-style query, 
		GREP-LIKE approach. Searches for specific bug - overflow in static char array allocations.

		""",
		# Description of query usage
		"""

		query usage


		""")



	QUERYLIST = [QUERY1, QUERY2, QUERY3, QUERY4, QUERY5, QUERY6]

	def getQueryList(self):
		return MDQueryRepository.QUERYLIST







