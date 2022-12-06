import * as React from 'react';
import Box from '@mui/material/Box';
import FormLabel from '@mui/material/FormLabel';
import FormControl from '@mui/material/FormControl';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormHelperText from '@mui/material/FormHelperText';
import Checkbox from '@mui/material/Checkbox';
import { useSelector, useDispatch } from 'react-redux'
import { updateTopics, deleteTopics, deleteAllTopics } from '../redux/slicers/topics'

export default function Topics() {

  const selectedTopics = useSelector((state) => state.topics.selectedTopics)
  const dispatch = useDispatch()

  const handleChange = (event) => {
    if (event.target.name !== 'all') {
      dispatch(deleteTopics('all'))
    } else {
      dispatch(deleteAllTopics())
    }
    event.target.checked === true
      ? dispatch(updateTopics(event.target.name))
      : dispatch(deleteTopics(event.target.name))
  };

  const error = selectedTopics.length < 1;

  return (
    <Box sx={{ display: 'flex' }}>
      <FormControl
        sx={{ m: 3 }}
        component="fieldset"
        variant="standard"
        error={error}
      >
        <FormLabel component="legend">Topics</FormLabel>
        <FormGroup>
          <FormControlLabel
            control={
              <Checkbox checked={selectedTopics.includes('politics')} onChange={handleChange} name="politics" />
            }
            label="Politics"
          />
          <FormControlLabel
            control={
              <Checkbox checked={selectedTopics.includes('technology')} onChange={handleChange} name="technology" />
            }
            label="Technology"
          />
          <FormControlLabel
            control={
              <Checkbox checked={selectedTopics.includes('education')} onChange={handleChange} name="education" />
            }
            label="Education"
          />
          <FormControlLabel
            control={
              <Checkbox checked={selectedTopics.includes('environment')} onChange={handleChange} name="environment" />
            }
            label="Environment"
          />
          <FormControlLabel
            control={
              <Checkbox checked={selectedTopics.includes('healthcare')} onChange={handleChange} name="healthcare" />
            }
            label="Healthcare"
          />
          <FormControlLabel
            control={
              <Checkbox checked={selectedTopics.includes('all')} onChange={handleChange} name="all" />
            }
            label="All"
          />
        </FormGroup>
        <FormHelperText>Select at least one topic.</FormHelperText>
      </FormControl>
    </Box>
  );
}
