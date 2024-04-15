import { mount, createLocalVue } from '@vue/test-utils';
import Watched from '@/views/Watched.vue'; // Assuming your component file path is correct

// Create a local Vue instance
const localVue = createLocalVue();

describe('Watched.vue', () => {
  let wrapper;

  // Mount the component before each test
  beforeEach(() => {
    wrapper = mount(Watched, {
      localVue,
    });
  });

  // Test if the component renders child components
  it('renders child components', () => {
    expect(wrapper.findComponent({ name: 'NavBar' }).exists()).toBe(true);
    expect(wrapper.findComponent({ name: 'EntryField' }).exists()).toBe(true);
    expect(wrapper.findComponent({ name: 'FilmGallery' }).exists()).toBe(true);
  });

  // Test if data is initialized correctly
  it('initializes with an empty films array', () => {
    expect(wrapper.vm.$data.films).toEqual([]);
  });

  // Test if fetchFilms method fetches films correctly
  it('fetches films and updates films array', async () => {
    // Mock axios
    const mockFilms = [{ id: 1, title: 'Film 1' }, { id: 2, title: 'Film 2' }];
    const axiosGet = jest.spyOn(wrapper.vm.$axios, 'get').mockResolvedValue({ data: mockFilms });

    // Trigger fetchFilms method
    await wrapper.vm.fetchFilms();

    // Check if films array is updated
    expect(wrapper.vm.$data.films).toEqual(mockFilms);

    // Check if axios.get is called with correct URL
    expect(axiosGet).toHaveBeenCalledWith('http://127.0.0.1:8000/films/');
  });

  // Test if films are displayed in FilmGallery component
  it('displays films in FilmGallery component', async () => {
    const mockFilms = [{ id: 1, title: 'Film 1' }, { id: 2, title: 'Film 2' }];
    wrapper.setData({ films: mockFilms });

    // Wait for next tick to ensure Vue has re-rendered the component
    await wrapper.vm.$nextTick();

    // Check if FilmGallery component displays films
    const filmGallery = wrapper.findComponent({ name: 'FilmGallery' });
    expect(filmGallery.exists()).toBe(true);
    expect(filmGallery.props('films')).toEqual(mockFilms);
  });
});
