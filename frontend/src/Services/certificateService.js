import axios from "axios"

const baseUrl = process.env.REACT_APP_BACKEND_URL + "api/certificates/"

const getAllCertificates = () => {
  const request = axios.get(baseUrl)
  return request.then((response) => response.data)
}

const createCert = async (newObject) => {
  const request = await axios.post(baseUrl, newObject)
  
  //console.log("req", request.data) 
  return request.data
}

const getSelectedCert =  (id) => {
  const request = axios.get(`${baseUrl}${id}/`)
  return request.then((response) => response.data)
}
const getSelectedCertByName =  (name) => {
  const request = axios.get(`${baseUrl}?certificate=${name}`)
  return request.then((response) => response.data)
}
//const editTech = (id, payload) => {
//    //Todo if we need it
//}

export default {
  getAllCertificates,
  createCert,
  getSelectedCert,
  getSelectedCertByName,
//  editConsultant,
}
