import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  selectedTopics: ['all']
}

export const topicsSlice = createSlice({
  name: 'topics',
  initialState,
  reducers: {
    updateTopics: (state, params) => {
      const { payload } = params
      state.selectedTopics = [...state.selectedTopics, payload]
    },
    deleteTopics: (state, params) => {
      const { payload } = params
      state.selectedTopics = state.selectedTopics
        .filter(selectTopic => selectTopic !== payload)
    },
    deleteAllTopics: (state, params) => {
      state.selectedTopics = []
    }
  }
})

export const { updateTopics, deleteTopics, deleteAllTopics } = topicsSlice.actions

export default topicsSlice.reducer
