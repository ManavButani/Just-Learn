"""this file contains the all graphql query related information
"""

USERS_PAYLOAD = """
                query ($email: String) {
                    getUserDetail(email: $email) {
                        Id
                        empCode
                        firstName
                        lastName
                        email
                        contactNumber
                        designation
                        directManager
                        __typename
                        directManagerName
                    }
                }
        """


def user_variable(email):
    return {
        "email": email
    }


DESIGNATION_PAYLOAD = """
{
  dropdown(cocCode: "12") {
    cocCode
    value
    code
    cocDesc
    __typename
  }
}
"""

ALL_USERS_PAYLOAD = """
                query ($status: [Int]) {
                    allUser(status: $status) {
                        Id
                        empCode
                        firstName
                        lastName
                        email
                        contactNumber
                        designation
                        directManager
                        __typename
                        directManagerName
                    }
                }
        """

ALL_USERS_VARIABLES = {"status": [1]}
