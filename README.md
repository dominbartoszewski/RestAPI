Library used for testing API requests: unittest.

| Tests                            | Description                          |
| ---------------------------------|:------------------------------------:|
| test_returns_200                 | Test if response code is 200         |
| test_check_dictionary            | Check if response body is dictionary |
| test_check_response_is_not_empty | Check if response body is not empty  |
| test_check_response_key          | Check if response key is "authors"   |

Why that validation was used?

unittest - for simple verifying the correct operation of individual API elements. Individual tests are separate and do not rely on the results of previous tests.
requests - most common used requests library for python.
