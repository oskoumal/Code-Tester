
from model.Query import Query

class NPDQueryRepository(object):
	"""Defines graph database queries for Null-pointer dereference issues and access methods for their usage"""

	# Query object contains: Number, Name, Code, Description, Usage
	QUERY1 = Query(
		# Number of query
		"1", 

		# Name
		"Minor issues (Null-pointer dereferences) for malloc/calloc near memcpy", 

		# Query code
		""" 

		import java.util.regex.Pattern;

		getCallsTo("memcpy")
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
		.filter{ it.code.contains("alloc") }

		.statements()
		.out("REACHES")
		.dedup()
		.match { it.type == "CallExpression" && it.code.startsWith("memcpy") }.ithArguments("2")

		.getCallsTo("memcpy")
		.ithArguments("0")
		.sideEffect{ arg = it.code; }

		.sideEffect{ sIdd = it.statements().toList()[0].id; }
		.unsanitized(
		{ it, s -> it._().or(
			_().isCheck('.*' + Pattern.quote(arg) + '.*'),
			_().codeContains('.*!.*' + Pattern.quote(arg)),
			_().codeContains(Pattern.quote(arg)))})

		.filter{ it.id != sIdd }
		.filter{ it.code.contains("alloc") }
		.filter{ !it.code.contains("xmalloc") }

		.dedup()	
		.locations()

		""",

		# General description
		"""

		todo
		
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
		"Minor issues (Null-pointer dereferences) for malloc/calloc near strcpy", 

		# Query code
		""" 

		import java.util.regex.Pattern;

		getCallsTo("strcpy")
		.ithArguments("1")
		.filter{ !it.argToCall().toList()[0].code.matches('.*(sizeof|min).*') }
		.sideEffect{ argument = it.code; }
		.sideEffect{ sId = it.statements().toList()[0].id; }
		.unsanitized(
		{ it, s -> it._().or(
			_().isCheck('.*' + Pattern.quote(argument) + '.*'),
			_().codeContains('.*lloc.*' + Pattern.quote(argument) + '.*'),
			_().codeContains('.*min.*'))})
		.filter{ it.id != sId }
		.filter{ it.code.contains("alloc") }

		.statements()
		.out("REACHES")
		.dedup()
		.match { it.type == "CallExpression" && it.code.startsWith("strcpy") }.ithArguments("1")

		.getCallsTo("strcpy")
		.ithArguments("0")
		.sideEffect{ arg = it.code; }

		.sideEffect{ sIdd = it.statements().toList()[0].id; }
		.unsanitized(
		{ it, s -> it._().or(
			_().isCheck('.*' + Pattern.quote(arg) + '.*'),
			_().codeContains('.*!.*' + Pattern.quote(arg)),
			_().codeContains(Pattern.quote(arg)))})

		.filter{ it.id != sIdd }
		.filter{ it.code.contains("alloc") }
		.filter{ !it.code.contains("xmalloc") }

		.dedup()	
		.locations()

		""",

		# General description
		"""

		todo
		
		""",

		# Description of query usage
		"""

		query usage


		""")

	
	QUERYLIST = [QUERY1, QUERY2]

	def getQueryList(self):
		return NPDQueryRepository.QUERYLIST







