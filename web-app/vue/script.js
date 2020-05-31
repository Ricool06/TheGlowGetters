// Load Vue single file components
httpVueLoader.register(Vue, '/vue/vega.vue');

// Map from region to name
region_name_map = {
  'hubei': 'Wuhan',
  'london': 'London',
  'nyc': 'New York'
}

// Map from region to AWS enpoints
region_aws_map = {
  'hubei': {
    'before': 'wuhan_before',
    'after': 'wuhan_after'
  },
  'london': {
    'before': 'china_test',
    'after': 'china_test'
  },
  'nyc': {
    'before': 'new_york_before',
    'after': 'new_york_after'
  }
}

// Initialize app
app = new Vue({
  el: '.app',
  data: function () {
    return {
      region: null,
      name: null,
      total_clustering_before: null,
      original_image_before: null,
      skeleton_image_before: null,
      total_isolated_filaments_before: null,
      total_clustering: null,
      original_image: null,
      skeleton_image: null,
      total_isolated_filaments: null
    }
  },
  methods: {
    load_region: function (region) {
      // Set the region
      this.region = region;
      this.name = region_name_map[region];
      
      // Fetch the data from before restrictions
      fetch(`https://aql10bbji4.execute-api.eu-central-1.amazonaws.com/prod/images/${region_aws_map[region].before}`)
      .then(response => response.json())
      .then(json => {
        data = json.Items[0];
        this.total_clustering_before = data.total_clustering.N;
        this.original_image_before = `https://space-apps-imagery.s3.eu-west-2.amazonaws.com/${data.original_image.S}`;
        this.skeleton_image_before = `https://space-apps-imagery.s3.eu-west-2.amazonaws.com/${data.skeleton_image.S}`;
        this.total_isolated_filaments_before = data.total_isolated_filaments.N;
      });
      
      // Fetch the data from during restrictions
      fetch(`https://aql10bbji4.execute-api.eu-central-1.amazonaws.com/prod/images/${region_aws_map[region].after}`)
      .then(response => response.json())
      .then(json => {
        data = json.Items[0];
        this.total_clustering = data.total_clustering.N;
        this.original_image = `https://space-apps-imagery.s3.eu-west-2.amazonaws.com/${data.original_image.S}`;
        this.skeleton_image = `https://space-apps-imagery.s3.eu-west-2.amazonaws.com/${data.skeleton_image.S}`;
        this.total_isolated_filaments = data.total_isolated_filaments.N;
      });
    }
  },
  mounted: function () {
  },
  created() {
  }
});
