import { configureStore } from '@reduxjs/toolkit'
import topicsReducer from './slicers/topics'

export const store = configureStore({
  reducer: {
    topics: topicsReducer,
  },
})
