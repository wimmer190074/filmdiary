import '@testing-library/jest-dom';

// Set up global mocks or stubs
jest.mock('axios', () => ({
  get: jest.fn().mockResolvedValue({ data: {} }),
}));
