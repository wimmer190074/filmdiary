module.exports = {
  // The root of your source code, typically the `src` directory
  roots: ['<rootDir>'],

  // Jest transformation for Vue.js files
  transform: {
    '^.+\\.vue$': 'vue-jest',
    '^.+\\.js$': 'babel-jest',
  },

  // Module file extensions
  moduleFileExtensions: ['js', 'vue'],

  // Test environment
  testEnvironment: 'jest-environment-jsdom',

  // Test regex pattern to match test files
  testRegex: '\./src/tests/.*\.test\.js$',

  // Test runner configuration
  // For example, if you're using Vue 3 with Composition API
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
  },

  // setupFiles: ['<rootDir>/tests/setup.js'], // If you have any setup file

  // Watch plugins
  watchPlugins: [
    'jest-watch-typeahead/filename',
    'jest-watch-typeahead/testname',
  ],
};
