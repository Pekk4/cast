import { createSlice } from "@reduxjs/toolkit"
import techService from "../Services/techService"
import consultantService from "../Services/consultantService"

const initialState = {
  editable: false,
  newSkillAddable: false,
  skillChanges: [],
  addableSkillDetail: null,//{new_skill_level: "", new_skill_name: ""}
  allSkills: null,//from consultant

}

const skillCardSlice = createSlice({
  name: "skillCard",
  initialState,
  reducers: {
    updateEditability(state, action) {
      return {
        ...state,
        editable: action.payload,
      }
    },
    updateNewSkillAddability(state, action){
      return {
        ...state,
        newSkillAddable: action.payload
      }
    },
    setSkillChanges(state,action) {
      return {
        ...state,
        skillChanges: action.payload
      }
    },
    setAddableSkillDetail(state, action){
      return{
        ...state,
        addableSkillDetail: action.payload
      }
    },
    setAllSkills(state,action){
      return{
        ...state,
        allSkills: action.payload
      }
    }
  },
})

export const initializeSkillCard = (id) => {
  return async (dispatch) => {
    const consultant = await consultantService.getSelectedConsultant(id)
    const skills = consultant.skills
    dispatch(setAllSkills(skills))
  }
}

export const {
  updateEditability,
  updateNewSkillAddability,
  setSkillChanges,
  setAddableSkillDetail,
  setAllSkills
} = skillCardSlice.actions

export default skillCardSlice.reducer

