/**
 * Get all dealerships
 */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
      const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
      const cloudant = CloudantV1.newInstance({
          authenticator: authenticator
      });
      cloudant.setServiceUrl(params.COUCH_URL);
      
      try {

        let list = await cloudant.postAllDocsQueries({db: 'dealerships',includeDocs: true})
        /**
        cloudant.getDatabaseInformation({db: 'dealerships'})
        .then(response => {
            console.log(response.result);
          });
        
        let dbList = await cloudant.getAllDbs();
        let mydb = await cloudant.db.use('dealerships');
        
        var q = "SELECT * from dealerships"
        mydb.query(q).then(console.log)
        */
        return { "dbs": list.result };
      } catch (error) {
          return { error: error.description };
      }
}

