JSONObjectactual = newJSONObject();
actual.put("id", 1);
actual.put("name", "mkyong");
actual.put("age", 37);

JSONAssert.assertEquals("{Base URL:https://groceries.morrisons.com/browse}", actual, false); 					//Pass, extended fields doesn't matter
JSONAssert.assertEquals("{name:\"mkyong\"}", actual, false);		//Pass
JSONAssert.assertEquals("{name:\"mkyong\", age:37}", actual, false);//Pass
JSONAssert.assertEquals("{name:mkyong, id:1}", actual, false);		//Pass
JSONAssert.assertEquals("{id:1, age:37}", actual, false);			//Pass